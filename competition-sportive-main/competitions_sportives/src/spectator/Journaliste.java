package spectator;

public class Journaliste implements SpectatorListener{
	
	@Override
	public void recupResultats(MatchTermineEvent e) {
		System.out.println( e.getP1().getName() + " vs " + e.getP2().getName() + " : " + e.getW().getName() + " wins !");	
	}
}
