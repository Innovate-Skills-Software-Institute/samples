import java.util.concurrent.ExecutionException;
import java.util.concurrent.StructuredTaskScope;

public class StructuredConcurrency {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
                try(StructuredTaskScope.ShutdownOnSuccess<String> scope = new StructuredTaskScope.ShutdownOnSuccess<>()){
            scope.fork(() -> "result1".substring(-1));
            scope.fork(() -> "result2");
            scope.join();
            System.out.println(scope.result());
        }

        try(StructuredTaskScope.ShutdownOnFailure scope = new StructuredTaskScope.ShutdownOnFailure()){
            StructuredTaskScope.Subtask<String> methodChild1 = scope.fork(() -> "result1".substring(-1));
            StructuredTaskScope.Subtask<String> methodChild2 = scope.fork(() -> "result2");
            scope.join();
            scope.throwIfFailed();
            System.out.println(methodChild1.get()+methodChild2.get());
        }
    }
}
