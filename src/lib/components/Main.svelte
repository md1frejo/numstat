<script>
 import Center from "$lib/components/Center.svelte"
 import stats from '$lib/data/stats.json';
 
 const st=Object.entries(stats)
 const st2=Object.entries(stats).flatMap(([outerKey, inner]) =>
   Object.entries(inner).map(([innerKey, value]) => [outerKey, innerKey, value])
 )
 const cts=Object.entries(stats).map(x => x[0])
 const deb=Object.entries(stats['Afghanistan']).map(x => x[0])
 
 let rand=Math.random()
 let fl=Math.floor()
 let placeh="place holder"
 
 function randFacts(cts,stats) {

   let ri=Math.floor(Math.random()*cts.length);
   let ct=cts[ri]
   let key="Median age"
   let st1=stats[ct][key]
   
//   let res1=stats[ct][key].match(/\d+/)
//   let st1=res1?res1:"nothing"
   
   return {country:ct,stat:st1}
 }

</script>

<style>
</style>

<main class="container px-4 max-w-cw1 mx-auto text-center bg-browngrad-800">
  <p class="text-4xl">debug: {placeh}</p>
  <p class="text-4xl">
    (country || city): {randFacts(cts,stats).country}  
    GDP/capita:
  </p>
  <p class="text-4xl">
    {randFacts(cts, stats).stat}
  </p>
  <p class="text-8xl">main</p>
  <Center stats={stats}/>
</main>
