package test;

import competition.AbstractCompetition;
import competition.Competitor;
import competition.League;

import java.util.List;  
    
public class LeagueTest extends AbstractCompetitionTest{

    @Override
    protected AbstractCompetition createComp(List<Competitor> competitors){
        return new League(competitors);
    }
   
}
    