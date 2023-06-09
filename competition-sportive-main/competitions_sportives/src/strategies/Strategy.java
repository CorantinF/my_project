package strategies;

import competition.Competitor;
import java.util.List;

public interface Strategy {
    public List<Competitor> selection();
}
