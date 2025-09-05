<script>
 import Left from "$lib/components/Left.svelte"
 import Datadisp from "$lib/components/Datadisp.svelte"

 export let stats
 export let bgleft=""
 export let bgdisp=""
 export let bgcenter=""
 export let bginnercenter=""
 
</script>

<main class={`container px-4 py-10 w-[1550px] mx-auto text-center ${bgcenter}`}>
  <section class={`border-4 border-dotted border-purple4g-800 rounded-xl p-4 ${bginnercenter} mx-auto w-2/3 min-h-32`}>
    <p class="text-ca1">Click on the different countries for stats</p>
    <p class="text-ca1">and to the left are some random ones</p>

  </section>
</main>

<div class="flex container mx-auto">
  <Left bgleft={bgleft} bg3="bg-blue-500" classn="w-1/5" stats={stats} />
  <Datadisp bgdisp={bgdisp} classn="w-4/5" stats={stats} />
</div>
