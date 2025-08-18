<script>
 export let stats;
 export let classn = "";

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

<main class={`bg-AntiqueWhiteg-200 ${classn}`}>
  <p class="text-4xl text-center text-brown4g-300">datadisp</p>

  {#each Object.entries(stats) as [country, details]}
    <p class="font-bold text-blueg-400 mt-6">Country: {country}</p>

    {#each chunk(Object.entries(details), 4) as group}
      <div class="grid grid-cols-4 gap-4 my-2">
        {#each group as [key, value]}
          {#if key === "Location"}
            <div><strong>{key}:</strong> {value}</div>
          {:else}
            <div>
              <button
                class="underline text-blue-600"
                on:click={() => toggleValue(country, key)}
		>
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
  {/each}
</main>
