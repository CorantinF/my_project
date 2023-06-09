package test;

import org.junit.*;

import competition.AbstractCompetition;
import competition.Competitor;
import competition.InadequateNbPlayerException;

import java.util.ArrayList;
import java.util.List;

public abstract class AbstractCompetitionTest {
    protected abstract AbstractCompetition createComp(List<Competitor> competitors);

    @Test
    public void createCompetitionTest() {
        List<Competitor> competitors = new ArrayList<Competitor>();
        competitors.add(new Competitor("a"));
        competitors.add(new Competitor("b"));
        competitors.add(new Competitor("c"));
        competitors.add(new Competitor("d"));
        competitors.add(new Competitor("e"));
        competitors.add(new Competitor("f"));
        competitors.add(new Competitor("g"));
        competitors.add(new Competitor("h"));
        competitors.add(new Competitor("i"));
        competitors.add(new Competitor("j"));
        competitors.add(new Competitor("k"));
        competitors.add(new Competitor("l"));
        competitors.add(new Competitor("m"));
        competitors.add(new Competitor("n"));
        competitors.add(new Competitor("o"));
        competitors.add(new Competitor("p"));

        AbstractCompetition comp = createComp(competitors);
        
        comp.play();
        System.out.println(comp.ranking());
    }
    
    @Test(expected = InadequateNbPlayerException.class)
    public void createEmptyCompetitionTest() throws InadequateNbPlayerException{
        List<Competitor> competitors = new ArrayList<Competitor>();
        AbstractCompetition comp = createComp(competitors);     
        comp.play();
        System.out.println(comp.ranking());
    }
    
    
    
}