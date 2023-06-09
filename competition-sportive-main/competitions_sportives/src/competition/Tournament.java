package competition;

import java.util.ArrayList;
import java.util.List;

public class Tournament extends AbstractCompetition {
    
    /**
     * constructor for Tournament class
     * @param players the competitor's list
     */
    public Tournament(List<Competitor> players) {
        super(players);
    }

    /**
     * check if the number of competitor is valid (nbCompetitor == 2^n)
     * @param nbPlayers the number of competitors
     * @return true if the number of competitors is good, false otherwise
     */
    public Boolean playersPuissanceDeDeux(Integer nbPlayers) {
    	if (nbPlayers%3 == 0 || !(nbPlayers%2 == 0)) {
        	return false;
        } else {
        	return true;
        }
    }

    /**
     * play the tournament competition
     * @param players the competitor's list
     */
    @Override
    protected void play(List<Competitor> players) {
        int nbPlayers = players.size();
        if (!playersPuissanceDeDeux(nbPlayers) || players.isEmpty()) {
            throw new InadequateNbPlayerException("Cannot play a tournament with " + nbPlayers + " players.");
        } else {
            List<Competitor> winners = players;
            while(winners.size() != 1) {
            	winners = this.playRounds(winners);
            }
        }
    }

    /**
     * play a round of the tournament
     * @param players the competitor's list
     * @return the winners of the round
     */
    private List<Competitor> playRounds(List<Competitor> players) {
        List<Competitor> winners = new ArrayList<Competitor>(); 
        for (int i = 0; i < players.size(); i += 2){
            Competitor c1 = players.get(i);
            Competitor c2 = players.get(i+1);
            this.scheduleMatch(c1, c2);
            if (c1.getRanking() > c2.getRanking()){
                winners.add(c1);
            } else {
                winners.add(c2);
            }      
        }
        return winners;
    }
}
