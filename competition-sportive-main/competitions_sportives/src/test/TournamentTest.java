package test;

import competition.AbstractCompetition;
import competition.Competitor;
import competition.InadequateNbPlayerException;
import competition.Tournament;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;  
    
public class TournamentTest extends AbstractCompetitionTest{

    @Override
    protected AbstractCompetition createComp(List<Competitor> competitors){
        return new Tournament(competitors);
    }
   
    @Test(expected = InadequateNbPlayerException.class)
    public void nonPuissanceDeDeuxTest() throws Exception {
    	List<Competitor> competitors = new ArrayList<Competitor>();
    	competitors.add(new Competitor("a"));
        competitors.add(new Competitor("b"));
        competitors.add(new Competitor("c"));
        
        Tournament tournament = new Tournament(competitors);
        tournament.play();
    }
}
    