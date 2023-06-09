package strategies;

import java.util.ArrayList;
import java.util.List;

import competition.Competitor;
import competition.Tournament;

public class StratB implements Strategy {
	private List<List<Competitor>> poules = new ArrayList<List<Competitor>>();
	
    public StratB(List<List<Competitor>> poules) {
		this.poules = poules;
	}
    /**
     * on prend les 2 premiers de chaque poule + x troisieme pour avoir un nombre puissance de 2
     * C.U. : le resultat doit etre une puissance de 2
     */
    @Override
    public List<Competitor> selection() {
        List<Competitor> winners = new ArrayList<Competitor>();
        for (int i = 0; i < this.poules.size() ; i++) {
            //on prend les 2 premiers
            Competitor poolWinner = new Competitor(""); //premier de la poule
            Competitor poolSecond = new Competitor(""); //deuxieme de la poule
            for (int j = 1; j < this.poules.get(i).size(); j++) { //on commence par le deuxieme
                if (this.poules.get(i).get(j).getRanking() > poolWinner.getRanking()) {
                   poolWinner = this.poules.get(i).get(j);
                } else {  //nimporte quel joueur tant que c'est pas le premier
                    poolSecond = this.poules.get(i).get(j); //deuxieme de la poule
                }
            }
            winners.add(poolWinner);
            for (int j = 1; j < this.poules.get(i).size(); j++) { //on commence par le deuxieme
                //Si moins bon que le premier mais meilleur que les autres
                if ((poolSecond.getRanking() < this.poules.get(i).get(j).getRanking()) && (this.poules.get(i).get(j).getRanking() < poolWinner.getRanking())) {
                   poolSecond = this.poules.get(i).get(j);
                }
            }
            winners.add(poolSecond);
        } //donc la normalement on a les 2 premiers de chaque poule
        //on créée un tournoi osef pour pas devoir réécrire la fonction
        Tournament tournament = new Tournament(this.poules.get(0));
        Competitor troisieme = new Competitor(""); //troisieme de la poule
        //on ajoute les autres pour faire une puissance de 2
        while (!tournament.playersPuissanceDeDeux(winners.size())) {
            for (int i = 0; i < this.poules.size() ; i++) {
                for (int j = 1; j < this.poules.get(i).size(); j++) {
                	if( (!winners.contains(this.poules.get(i).get(j))) && (this.poules.get(i).get(j).getRanking() > troisieme.getRanking())) { 
                    	troisieme = this.poules.get(i).get(j);
                    }
                } 
            }
            winners.add(troisieme);
            troisieme = new Competitor("");
        }
        return winners;
    }    
}