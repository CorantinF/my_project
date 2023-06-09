package competition;

import java.util.List;

public class League extends AbstractCompetition {
    
    /**
     * constructor for League class
     * @param players the Competitors list
     */
    public League(List<Competitor> players) {
        super(players);
    }

    /**
     * play a League competition
     * @param players the competitors list
     */
    @Override
    protected void play(List<Competitor> players) {
    	if (!players.isEmpty()) {
	        for (int i = 0; i < players.size(); i++){
	            Competitor c1 = players.get(i);
	            for (int j = 0; j < players.size(); j++){
	                Competitor c2 = players.get(j);
	                if (! c1.equals(c2)){
	                    this.scheduleMatch(c1,c2);
	                }
	            }
	        }
    	} else {
    		 throw new InadequateNbPlayerException("Cannot play a league with " + players.size() + " players.");
    	}
    }
    
}
