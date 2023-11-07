public class Main {
    private static final ScopedValue<Integer> scopedValue = ScopedValue.newInstance(); // Defined as static final.

    public static void main(String[] args) {
        for(int j = 0; j < 3; j ++) {
            // Ideally You will call Application.handle(request,response) runnable task
            new Thread(() -> ScopedValue.where(scopedValue, (int) (Math.random() * 50D)).run(() -> {
                for (int i = 0; i < 3; i++) {
                    // Access Scoped Value
                    System.out.println(Thread.currentThread().getName()+" : "+scopedValue.get());
                    try {
                        Thread.sleep(500L);
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                }
            })).start();
        }
    }
}