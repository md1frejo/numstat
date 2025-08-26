<script>

 import { Flag,ArrowDownAZ } from "lucide-svelte"
 
 export let stats;
 export let classn = ""
 export let bgdisp=""
 
 let openItems = {};

 function toggleValue(country, key) {
   if (!openItems[country]) {
     openItems[country] = new Set();
   }
   if (openItems[country].has(key)) {
     openItems[country].delete(key); // close it
   } else {
     openItems[country].add(key); // open it
   }
   openItems = { ...openItems }; // force reactivity
 }

 // Helper: chunk an array into groups of 4
 function chunk(array, size) {
   const result = [];
   for (let i = 0; i < array.length; i += size) {
     result.push(array.slice(i, i + size));
   }
   return result;
 }
</script>

<main class={`${bgdisp} ${classn}`}>
  <div class="flex items-center justify-center space-x-4">
    <ArrowDownAZ class="w-10 h-10 text-blueg-600"/>
    <p class="text-4xl text-center text-brown4g-300">Countries</p>
    <ArrowDownAZ class="w-10 h-10 text-blueg-600"/>
  </div>
  <br>
  <br>
  {#each Object.entries(stats) as [country, details]}
    <div class="flex items-start justify-start space-x-4">
      <Flag class="w-7 h-7 text-browngrad-200"/>
      <p class="font-bold text-da1 text-browngrad-200 mt-6">{country} <p class="text-purple4g-200 text-da2 font-crimson"> {Object.entries(details)[1]} </p>
      </div>
      {#if Object.keys(details).length === 0}
	<p class="text-brown4g-300">missing</p>
      {:else}
	{#each chunk(Object.entries(details), 6) as group}
	  <div class="grid grid-cols-6 gap-4 my-1">
            {#each group as [key, value]}
              {#if key === "Location23432"}
		<div><p class="text-da1 text-browngrad-200">{key}:</p><p class="text-grey6g-200" >{value}</p></div>
              {:else}
		<div class="border-b-2 border-dotted border-grey6g-800">
		  <button class="underline text-blue-600" on:click={() => toggleValue(country,key)}>
                    {key}
		  </button>
		  {#if openItems[country] && openItems[country].has(key)}
                    <p class="text-brown4g-300">{value}</p>
		  {/if}
		</div>
              {/if}
            {/each}
	  </div>
	{/each}
      {/if}
  {/each}
</main>
