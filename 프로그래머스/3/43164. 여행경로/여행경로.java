import java.util.*;

class Solution {
    static boolean isFound = false;
    public String[] solution(String[][] ticketInfos) {
        String[] answer = new String[ticketInfos.length + 1];

        Arrays.sort(ticketInfos, (s1, s2) -> {
            if (!s1[0].equals(s2[0])) return s1[0].compareTo(s2[0]);
            else return s1[1].compareTo(s2[1]);
        });

        Map<String, List<Ticket>> ticketMap = new HashMap<>();
        for (String[] ticketInfo: ticketInfos) {
            String source = ticketInfo[0];
            String destination = ticketInfo[1];
            Ticket ticket = new Ticket(source, destination);

            if (!ticketMap.containsKey(source)) {
                List<Ticket> ticketList = new ArrayList<>();
                ticketMap.put(source, ticketList);
            }
            ticketMap.get(source).add(ticket);
        }

        answer[0] = "ICN";
        backTracking(1, ticketInfos.length + 1,
                "ICN", ticketMap, answer);

        return answer;
    }

    public void backTracking(int cnt, int targetCnt, String currentAirport,
                             Map<String, List<Ticket>> ticketMap, String[] answer) {
        // base case
        if (cnt == targetCnt) {
            isFound = true;
            return;
        }

        // destination이 없는 경우
        if (!ticketMap.containsKey(currentAirport)) return;

        for (Ticket ticket: ticketMap.get(currentAirport)) {
            if (ticket.used) continue;
            ticket.used = true;
            answer[cnt] = ticket.destination;
            backTracking(cnt + 1, targetCnt, ticket.destination, ticketMap, answer);
            if (isFound) return;
            answer[cnt] = null;
            ticket.used = false;
        }
    }

    class Ticket {
        String source;
        String destination;
        boolean used;

        Ticket(String source, String destination) {
            this.source = source;
            this.destination = destination;
            this.used = false;
        }
    }
}