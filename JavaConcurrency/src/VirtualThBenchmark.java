import java.util.ArrayList;
import java.util.Scanner;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.IntStream;

public class VirtualThBenchmark {
    public static void main(String[] args) {

        // Wait for VisualVm to connect
        new Scanner(System.in).nextLine();

        // Time Benchmarking Code
        long startTime = System.currentTimeMillis();
        Runtime.getRuntime().addShutdownHook(new Thread(()->{
            long endTime = System.currentTimeMillis();
            System.out.println("Total time taken : "+(endTime-startTime)+"ms");
        }));

        // Dummy Data Code
        IntStream intStream = IntStream.rangeClosed(0, 10000);

        // Actual Thread and ThreadPool Executor Code
        try (ExecutorService executorService = Executors.newVirtualThreadPerTaskExecutor()) {
            intStream.forEach(num -> {
                Runnable task = () -> {
                    ArrayList<Double> list = new ArrayList<>();
                    sleep();
                    for (int i = 1; i < num; i++) {
                        Double number = Math.pow(num, 3);
                        list.add(number);
                    }
                    sleep();
                };
                Thread vt = Thread.ofVirtual().start(task);
                executorService.submit(vt);
            });
        }
    };

    private static void sleep() {
        try {
            Thread.sleep(5L);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
