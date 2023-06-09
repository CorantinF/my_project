package spectator;

import java.util.EventListener;

public interface SpectatorListener extends EventListener{
	public void recupResultats(MatchTermineEvent e);
}
