public class CountPeptide {
    private int[] value;
    private int Min =Integer.MAX_VALUE;
    public CountPeptide(int[] v) {
        value = v;
        for (int i=0; i<value.length; i++) {
            if (Min>value[i]) Min=value[i];
        }
        StdOut.printf("Min_value: %d\n", Min);
    }
    private long count(int mass) {
        if (mass==0) {
            return 1;
        }
        if (mass<Min) {
            return 0;
        }
        long count=0;
        for (int i=0; i<value.length; i++) {
            count += count(mass-value[i]);
        }
        return count;
    }
    
    public long Count(int mass) {
        return count(mass);
    }
    
    public static void main(String[] args) {
        int[] v={57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186};
        CountPeptide cp = new CountPeptide(v);
        while (!StdIn.isEmpty()) {
            int m = StdIn.readInt();
            StdOut.printf("count(%d) = %d\n", m, cp.Count(m));
        }
    }
}
        
        