<script>

 export let stats
 
 const st=Object.entries(stats)
 const st2=Object.entries(stats).flatMap(([outerKey, inner]) =>
   Object.entries(inner).map(([innerKey, value]) => [outerKey, innerKey, value])
 )
 const cts=Object.entries(stats).map(x => x[0])
 const deb=Object.entries(stats['Afghanistan']).map(x => x[0])
 
 let rand=Math.random()
 let fl=Math.floor()
 let placeh="place holder"
 
 function randFacts(cts, stats) {
   while(true) {
     let ri = Math.floor(Math.random() * cts.length);
     let ct = cts[ri];
     let key = "Median age";

     if (stats[ct][key]) {
       let st1 = stats[ct][key];
       return { country: ct, stat: st1 }; 
     }
   }
 }

</script>

<style>
</style>

<main class="container px-4 py-10 max-w-cw1 mx-auto text-center bg-AntiqueWhiteg-500">
  <p class="text-redrose text-ma1">
    region: {randFacts(cts,stats).country}  median age: {randFacts(cts, stats).stat}
  </p>

</main>
