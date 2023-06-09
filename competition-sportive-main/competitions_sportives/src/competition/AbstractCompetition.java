package competition;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import match.AbstractMatch;
import match.RandomMatch;
import spectator.Bookmakers;
import spectator.Journaliste;
import util.MapUtil;

public abstract class AbstractCompetition implements Competition {
    private final AbstractMatch match;
    private final List<Competitor> players;
    protected final Map<Competitor, Integer> rankings = new HashMap<Competitor, Integer>();
    
    private Journaliste journaliste = new Journaliste();
    private Bookmakers bookmakers = new Bookmakers();
    /**
     * constructor for abstractCompetition class
     * @param players
     */
    protected AbstractCompetition(List<Competitor> players) {
        this.match = new RandomMatch(this);
        this.players = players;
        for (Competitor player : players) {
            rankings.put(player, 0);
        }
        this.match.addSpectatorListener(journaliste);
        this.match.addSpectatorListener(bookmakers);
    }

    /**
     * this method play a competition
     */
    public void play() {
        this.play(this.players);
        this.bookmakers.afficheResultats();
    }

    protected abstract void play(List<Competitor> players);

    /**
     * play a match between the 2 competitors in parameter
     * @param player1 a Competitor
     * @param player2 an other Competitor
     */
    protected void scheduleMatch(Competitor player1, Competitor player2) {
        this.match.play(player1, player2);
    }

    /**
     * add points to te Competitor in parameter
     * @param winner a Competitor
     */
    public void addPointsToWinner(Competitor winner) {
        this.rankings.put(winner, this.rankings.get(winner) + 1);
        winner.upgradeRankingByOne();
    }

    /**
     * this function return the players
     * @return the players
     */
    public List<Competitor> getPlayers() {
        return players;
    }

    /**
     * this function return the rank of the players
     * @return the rank of the players
     */
    public Map<Competitor, Integer> ranking() {
        return MapUtil.sortByDescendingValue(this.rankings);
    }
}