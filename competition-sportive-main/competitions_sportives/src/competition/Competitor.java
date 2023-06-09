package competition;

public class Competitor {
    private final String name;
    private int ranking;

    /**
     * constructor for competitor class
     * @param name the name of the competitor
     */
    public Competitor(String name) {
        this.name = name;
    }

    /**
     * return the name of the competitor
     * @return the name of this competitor
     */
    public String getName() {
        return this.name;
    }

    /**
     * return the ranking of the competitor
     * @return the ranking of the competitor
     */
    public int getRanking() {
        return this.ranking;
    }

    /**
     * upgrade the ranking of the competitor by one
     */
    public void upgradeRankingByOne() {
        this.ranking +=1;
    }

    /**
     * return the competitor to string
     * @return the competitor's name
     */
    @Override
    public String toString(){
        return this.name;
    }
}
