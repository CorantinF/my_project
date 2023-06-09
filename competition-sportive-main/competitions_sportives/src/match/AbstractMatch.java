package match;

import java.util.ArrayList;

import competition.AbstractCompetition;
import competition.Competitor;
import spectator.MatchTermineEvent;
import spectator.SpectatorListener;

public abstract class AbstractMatch implements Match{
    private AbstractCompetition competition;

    /**
     * constructor for the AbstractMatch class
     * @param competition a competition (League, Tournament, ...)
     */
    public AbstractMatch(AbstractCompetition competition) {
        this.competition = competition;
    }
    
    /**
     * play a match between two players
     * @param player1 a Competitor
     * @param player2 an other Competitor
     */
    //ca doit augmenter la cote
    public void play(Competitor player1, Competitor player2) {
        Competitor winner = peekWinner(player1, player2);
        competition.addPointsToWinner(winner);
        this.fireRecupResultats(player1,player2,winner); // on recup les resultats
    }
    
    //@TemplateMethod
    protected abstract Competitor peekWinner(Competitor player1, Competitor player2);
    
//	OBSERVER
    public ArrayList<SpectatorListener> spectatorListeners = new ArrayList<SpectatorListener>();
    
    /**
     * 
     * @param l
     */
    public synchronized void addSpectatorListener(SpectatorListener l) {
		if (spectatorListeners.contains(l)) { return; }
		spectatorListeners.add(l);
	}
	 
    /**
     * 
     * @param l
     */
	public synchronized void removeSpectatorListener(SpectatorListener l) {
		spectatorListeners.remove(l);
	}
	
	public ArrayList<SpectatorListener> getSpec(){
		return this.spectatorListeners;
	}
	
	/**
	 * 
	 */
	private void fireRecupResultats(Competitor player1, Competitor player2, Competitor winner) {
		@SuppressWarnings("unchecked")
		ArrayList<SpectatorListener> s1 = (ArrayList<SpectatorListener>) this.spectatorListeners.clone();
		if (s1.size() == 0) { return; }
		MatchTermineEvent event = new MatchTermineEvent(player1, player2, winner);
		for (SpectatorListener listener : s1) {
			listener.recupResultats(event);
		}
	}
	
	/**
	 * 
	 */
	public void diffuserResultat(Competitor player1, Competitor player2, Competitor winner) { fireRecupResultats(player1, player2, winner); }

}
