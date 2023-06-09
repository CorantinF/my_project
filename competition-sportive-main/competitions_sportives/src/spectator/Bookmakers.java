package spectator;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

import competition.Competitor;

public class Bookmakers  implements SpectatorListener {
	private Map<Competitor,Integer> cotes = new HashMap<Competitor,Integer>();
	
	@Override
	public void recupResultats(MatchTermineEvent e) {
		if (!cotes.containsKey(e.getP1())) {
			cotes.put(e.getP1(), 0);
		} 
		if (!cotes.containsKey(e.getP2())) {
			cotes.put(e.getP2(), 0);
		} 
		
		if (e.getW() == e.getP1()) {
			cotes.put(e.getP1(), cotes.get(e.getP1()) - 1);
			cotes.put(e.getP2(), cotes.get(e.getP2()) + 1);
		} else {
			cotes.put(e.getP1(), cotes.get(e.getP1()) + 1);
			cotes.put(e.getP2(), cotes.get(e.getP2()) - 1);
		}
		
	}
	
	public void afficheResultats() {
		if (!cotes.isEmpty()) {
			System.out.println("*** Côtes ***");
	        for(Entry<Competitor, Integer> entry : this.cotes.entrySet()) {
	            Competitor cle = entry.getKey();
	            Integer valeur = entry.getValue();
	            System.out.println(cle + " - " + valeur);
	        }
		}
	}
}