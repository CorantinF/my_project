package test;

import org.junit.*;
import static org.junit.Assert.*;

import competition.AbstractCompetition;
import competition.Competitor;
import competition.League;
import match.AbstractMatch;

import java.util.ArrayList;
import java.util.List;

public abstract class AbstractMatchTest {
    protected abstract AbstractMatch createMatch(AbstractCompetition competition);
    
    @Test
    public void CreateRandomMatchTest() {
        List<Competitor> players = new ArrayList<Competitor>();
        Competitor c1 = new Competitor("Abdel");
        Competitor c2 = new Competitor("Kader");     
        players.add(c1);
        players.add(c2);
        
        AbstractCompetition competition = new League(players);
        AbstractMatch match = createMatch(competition);

        match.play(c1, c2);
        if (c1.getRanking() == 1){
            assertEquals(c1.getRanking(),1);
            assertEquals(c2.getRanking(),0);
        } else {
            assertEquals(c2.getRanking(),1);
            assertEquals(c1.getRanking(),0);
        }
    }
}
