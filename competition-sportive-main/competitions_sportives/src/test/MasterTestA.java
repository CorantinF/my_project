package test;

import competition.AbstractCompetition;
import competition.Competitor;
import competition.Master;
import strategies.*;

import java.util.List;  
    
public class MasterTestA extends AbstractCompetitionTest{

    @Override
    protected AbstractCompetition createComp(List<Competitor> competitors){
        return new Master(competitors ,StratEnum.STRATA ,4 );
    }
   
}