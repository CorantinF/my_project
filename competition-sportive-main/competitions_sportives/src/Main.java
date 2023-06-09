import java.util.ArrayList;
import java.util.List;

import competition.Competitor;
import competition.League;
import competition.Master;
import competition.Tournament;
import strategies.StratEnum;

public class Main {
    public static void main(String[] args){   
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
        
        System.out.println("--- TEST LEAGUE ---");
        League league = new League(competitors);
        league.play();
        //league.displayResult(league.ranking());
        
        System.out.println("--- TEST TOURNAMENT ---");
        Tournament tournament = new Tournament(competitors);
        tournament.play();
        //tournament.displayResult(tournament.ranking());
        
        System.out.println("--- TEST MASTER A ---");
        Master masterA = new Master(competitors, StratEnum.STRATA, 4);
        masterA.play();
        //mastera.displayResult(mastera.ranking());
        
        competitors.add(new Competitor("q"));
        competitors.add(new Competitor("r"));
        competitors.add(new Competitor("s"));
        competitors.add(new Competitor("t"));
        
        competitors.add(new Competitor("u"));
        competitors.add(new Competitor("v"));
        competitors.add(new Competitor("w"));
        competitors.add(new Competitor("x"));
        
        System.out.println("--- TEST MASTER B ---");
        Master masterB = new Master(competitors, StratEnum.STRATB, 3);
        masterB.play();
        //masterb.displayResult(masterb.ranking());
        
    }
}