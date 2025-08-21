<script>
 import { AlignVerticalSpaceAround,AlignHorizontalJustifyEnd,AlignHorizontalJustifyStart,Merge } from "lucide-svelte";
 // https://lucide.dev/icons/align-vertical-space-around

 export let bgtop=""
 
</script>

<style>
</style>

<section class={`${bgtop} py-1 w-[1530px] mx-auto px-1`}>

  <div class="flex items-center justify-center space-x-4">
    <Merge class="w-20 h-20 text-blueg-600"/>
    <p class="text-top1 text-blueg-200">numstats</p>
    <Merge class="w-20 h-20 text-blueg-600"/>
</div>
</section>
