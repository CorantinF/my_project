package test;

import competition.AbstractCompetition;
import match.AbstractMatch;
import match.RandomMatch;

public class RandomMatchTest extends AbstractMatchTest{

    @Override
    protected AbstractMatch createMatch(AbstractCompetition competition){
        return new RandomMatch(competition);
    }   
}
    