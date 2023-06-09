package test;

import org.junit.*;
import static org.junit.Assert.*;

import competition.Competitor;
    
public class CompetitorTest {

    @Test
    public void createCompetitorTest() {
        Competitor c = new Competitor("Albert");
        assertSame(c.getName(),"Albert");
    }

    
}
    