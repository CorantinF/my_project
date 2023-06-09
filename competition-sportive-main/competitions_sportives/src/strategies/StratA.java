package strategies;

import java.util.List;
import java.util.ArrayList;

import competition.Competitor;

public class StratA implements Strategy {
    private List<List<Competitor>> poules = new ArrayList<List<Competitor>>();
	
    public StratA(List<List<Competitor>> poules) {
		this.poules = poules;
	}
	
	/**
     * on prend juste le meilleur de chaque poule
     * C.U. : le resultat doit etre une puissance de 2
     */
    @Override
    public List<Competitor> selection() {       
        List<Competitor> winners = new ArrayList<Competitor>();
        for (int i = 0; i < this.poules.size() ; i++) {
            Competitor poolWinner = this.poules.get(i).get(0); //premier de la poule
            for (int j = 1; j < this.poules.get(i).size(); j++) { //on commence par le deuxieme
                if (this.poules.get(i).get(j).getRanking() > poolWinner.getRanking()) {
                   poolWinner = this.poules.get(i).get(j);
                }
            }
            winners.add(poolWinner);
        }
        return winners;
    }	
}
