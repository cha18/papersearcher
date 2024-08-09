<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})



const count = ref(0)
</script>

<template>
<label
    class="mx-auto mt-40 relative bg-slate-700 min-w-sm flex flex-col md:flex-row items-center justify-center border-black py-2 px-2 rounded-2xl gap-2 duration-700  hover:shadow-2xl hover:shadow-slate-800 focus-within:border-black"
    for="search-bar">
    <input v-on:keyup.enter="search" id="search-bar" v-model="searchText" :placeholder="showSearchIsEmpty ? 'This cannot be left empty.' : 'Search papers...'"
    :class="{ 'px-6 py-2 w-full rounded-md flex-1 outline-none bg-slate-700 custom-autofill text-white': true, 'placeholder-red-600': showSearchIsEmpty}">
    <button
        class="w-full md:w-auto px-6 py-3 bg-black border-black text-white fill-gray-500 active:scale-95 duration-100 border will-change-transform overflow-hidden relative rounded-xl transition-all disabled:opacity-70" @click="search">
        
        <div class="relative">

            <!-- Loading animation change opacity to display -->
            <div
                class="flex items-center justify-center h-3 w-3 absolute inset-1/2 -translate-x-1/2 -translate-y-1/2 transition-all">
                <svg class="opacity-0 animate-spin w-full h-full" xmlns="http://www.w3.org/2000/svg" fill="none"
                    viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor"
                        stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor"
                        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                    </path>
                </svg>
            </div>

            <div class="flex items-center transition-all opacity-1 valid:"><span
                    class="text-sm font-monospace whitespace-nowrap truncate mx-auto">
                    Search
                </span>
            </div>

        </div>
        
    </button>
</label>

</template>


<script>
import eventBus from './eventBus.js';

export default {
  data() {
    return {
      searchText: '',
      showSearchIsEmpty: false
    };
  },
  methods: {
    search() {
      if (this.searchText == '') {
        console.log("reached")
          this.showSearchIsEmpty = true;
          return;
      }
      eventBus.emit('custom-event', this.searchText);
    },
  },
};
</script>


<style scoped>


.read-the-docs {
  color: #888;
}

.custom-autofill:-webkit-autofill {
    transition: background-color 5000s ease-in-out 0s;
    --tw-bg-opacity: 1;
    background-color: rgb(51 65 85 / var(--tw-bg-opacity)) !important;
  }

  .custom-autofill:-webkit-autofill::first-line {
    color: #ffffff !important;
}
</style>
