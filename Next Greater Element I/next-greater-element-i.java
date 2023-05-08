/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    let result = [];
    for(let num of nums1)
    {
        let flag=-1;
        for(let i=nums2.indexOf(num)+1;i<nums2.length;i++)
        {
            if(nums2[i]>num)
            {
                flag=nums2[i];
                break;
            }
        }
        result.push(flag);
    }
    return result;
};