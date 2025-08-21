<script>
 import Main from "$lib/components/Main.svelte"
 import Center from "$lib/components/Center.svelte"
 import stats from '$lib/data/stats.json';

 export let data
 
</script>

<Main bgmain={data.bgmain} stats={stats} />
<Center bgcenter={data.bgcenter} bgleft={data.bgleft} bgdisp={data.bgdisp} stats={stats}/>

<main class="container mx-auto px-4 flex gap-4">

</main>





