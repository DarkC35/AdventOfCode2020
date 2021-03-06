<h2 id="part2">Part Two</h2>
<p>The final step in breaking the XMAS encryption relies on the invalid number you just found: you must <em>find a contiguous set of at least two numbers</em> in your list which sum to the invalid number from step 1.</p>
<p>Again consider the above example:</p>
<pre><code>35
20
<em>15</em>
<em>25</em>
<em>47</em>
<em>40</em>
62
55
65
95
102
117
150
182
127
219
299
277
309
576
</code></pre>
<p>In this list, adding up all of the numbers from <code>15</code> through <code>40</code> produces the invalid number from step 1, <code>127</code>. (Of course, the contiguous set of numbers in your actual list might be much longer.)</p>
<p>To find the <em>encryption weakness</em>, add together the <em>smallest</em> and <em>largest</em> number in this contiguous range; in this example, these are <code>15</code> and <code>47</code>, producing <em><code>62</code></em>.</p>
<p><em>What is the encryption weakness in your XMAS-encrypted list of numbers?</em></p>
<p>Your puzzle answer was <code>3012420</code>.</p>

Source: https://adventofcode.com/2020/day/9#part2