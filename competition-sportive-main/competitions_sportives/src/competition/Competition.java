package competition;

import java.util.Map;

public interface Competition {
    void play();

    Map<Competitor, Integer> ranking();
}
