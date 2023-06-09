package test;

import competition.AbstractCompetition;
import competition.Competitor;
import competition.Master;
import strategies.*;

import java.util.List;  
    
public class MasterTestB extends AbstractCompetitionTest{

    @Override
    protected AbstractCompetition createComp(List<Competitor> competitors){
        return new Master(competitors ,StratEnum.STRATB ,3 );
    }
   
}