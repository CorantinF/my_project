package spectator;

import java.util.EventObject;

import competition.Competitor;

public class MatchTermineEvent extends EventObject{
	private static final long serialVersionUID = 1L;
	private Competitor winner;
	private Competitor player1;
	private Competitor player2;
	
	public MatchTermineEvent(Competitor p1, Competitor p2, Competitor w) {
		super(w);
		this.player1 = p1;
		this.player2 = p2;
		this.winner = w;
	}
	
	public Competitor getP1() {
		return this.player1;
	}
	
	public Competitor getP2() {
		return this.player2;
	}
	
	public Competitor getW() {
		return this.winner;
	}
	
}
