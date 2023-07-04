public class Solution {
    public IList<IList<int>> KSmallestPairs(int[] nums1, int[] nums2, int k) {
        
        PriorityQueue<(int,int),int> pq = new PriorityQueue<(int,int),int>(Comparer<int>.Create((a,b)=>b-a));

        for(int i=0;i<nums1.Length;i++)
        {
            for(int j=0;j<nums2.Length;j++)
            {
                if(pq.TryPeek(out (int n1,int n2) value,out int p) && pq.Count >= k && p<nums1[i]+nums2[j])
                {
                    break;
                }
                
                pq.Enqueue((nums1[i],nums2[j]),nums1[i]+nums2[j]);                
                if(pq.Count>k)
                {
                    pq.Dequeue();
                }
            }
        }

        List<IList<int>> result = new ();
        while(pq.TryDequeue(out (int n1,int n2) value,out int p))
        {
            result.Add(new List<int>(){value.n1,value.n2});
        }

        return result;
    }
}