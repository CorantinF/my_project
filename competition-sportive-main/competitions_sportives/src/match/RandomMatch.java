package match;

import competition.AbstractCompetition;
import competition.Competitor;

public class RandomMatch extends AbstractMatch implements Match{
    
    /**
     * constructor for RandomMatch class
     * @param competition a competition (League, Tournament, ...)
     */
    public RandomMatch(AbstractCompetition competition) {
        super(competition);
    }

    /**
     * peek a winner between two players
     * @param player1 a Competitor
     * @param player2 an other competitor
     * @return the winner
     */
    protected Competitor peekWinner(Competitor player1, Competitor player2) {
        int result = (int) ((Math.random() * (2 - 0)) +0);
        if(result > 0) {
            return player1;
        } else {
            return player2;
        }
    }
}
