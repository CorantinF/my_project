package competition;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import strategies.*;

public class Master extends AbstractCompetition {
    private StratEnum strat; // methode de selection des joueurs
    private Integer nbPoules;

    /**
     * constructor for Master class
     * @param players the competitor's list
     * @param strat the strategy of the master
     * @param nbPoules the number of groupe
     */
    public Master(List<Competitor> players, StratEnum strat, Integer nbPoules) {
        super(players);
        this.strat = strat;
        this.nbPoules = nbPoules;
    }

    /**
     * play the Match competition
     * @param players the competitor's list
     */
    @Override
    protected void play(List<Competitor> players) {
    	if (!players.isEmpty()) {
	        League league = new League(players);
	        league.play();
	        this.majRankings(league.ranking());
	        //actualiser les points avec une fonction
	        //this.rankings = league.ranking();
	        
	        //choix des poules
	        List<List<Competitor>> poules = new ArrayList<List<Competitor>>();
	        poules = makePoules(players);
	        
	        // choix finalistes
	        List<Competitor> finalists = new ArrayList<Competitor>();
	        finalists = chooseStrat(poules);
	        // finale
	        Tournament tournament = new Tournament(finalists);
	        tournament.play();
	        this.majRankings(tournament.ranking());
    	} else {
    		 throw new InadequateNbPlayerException("Cannot play a master with " + players.size() + " players.");    	}
    }

    /**
     * make groupe about the competitor's list
     * @param players the competitor's list
     * @return the list of groupe
     */
    private List<List<Competitor>> makePoules(List<Competitor> players) {
        List<List<Competitor>> poules = new ArrayList<List<Competitor>>();
        Integer taillePoule = players.size() / this.nbPoules;
        Integer cmp = 0;
        for (int i = 0; i < this.nbPoules; i++) {
            List<Competitor> poule = new ArrayList<Competitor>();
            for (int j = 0; j < taillePoule; j++) {
                poule.add(players.get(cmp));
                cmp++;
            }
            poules.add(poule);
        }
        return poules;
    }

    /**
     * take an enum and return the associated strategy 
     * @return a strategy
     */
    private List<Competitor> chooseStrat(List<List<Competitor>> poules){
    	switch (this.strat){
            case STRATA:
                 Strategy s = new StratA(poules);
                 return s.selection();
            case STRATB:
                s = new StratB(poules);
                return s.selection();
            default :
            	return null;
        }
    }
    
    private void majRankings(Map<Competitor, Integer> rankings) {
    	for(Entry<Competitor, Integer> entry : rankings.entrySet()) {
            Competitor cle = entry.getKey();
            Integer value = entry.getValue();
            for (int i = 0; i < value; i++) {
            	this.addPointsToWinner(cle); 
            }           
        }
    }
    
}
