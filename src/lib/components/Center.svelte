<script>
 import Left from "$lib/components/Left.svelte"
 import Datadisp from "$lib/components/Datadisp.svelte"

 export let stats
 
</script>

<main class="container px-4 py-10 max-w-cw1 mx-auto text-center bg-AntiqueWhiteg-400">
  <p class="text-4xl">center</p>
</main>

<div class="flex container mx-auto">
  <Left classn="w-1/4" />
  <Datadisp classn="w-3/4" stats={stats} />
</div>
