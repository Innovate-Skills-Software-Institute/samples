import javax.crypto.DecapsulateException;
import javax.crypto.KEM;
import java.security.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException, DecapsulateException {
        // Receiver side
        var kpg = KeyPairGenerator.getInstance("X25519"); // ECDH
        var kp = kpg.generateKeyPair();

        // Sender side
        var kem1 = KEM.getInstance("DHKEM");
        var sender = kem1.newEncapsulator(kp.getPublic());
        var encapsulated = sender.encapsulate();
        var k1 = encapsulated.key();

        // Receiver side
        var kem2 = KEM.getInstance("DHKEM");
        var receiver = kem2.newDecapsulator(kp.getPrivate());
        var k2 = receiver.decapsulate(encapsulated.encapsulation());

        assert Arrays.equals(k1.getEncoded(), k2.getEncoded());
    }
}