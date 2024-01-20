<script setup>
import { ref } from 'vue'
import SearchBar from './SearchBar.vue'
import NavBar from './NavBar.vue'

defineProps({
  msg: String,
})

const count = ref(0)


</script>

<template>
    <div class="bg-gray-900 text-white font-spacemono">
        <div id="navbarComponent" class="bg-blue-500 text-white p-4 fixed z-50">
            <NavBar></NavBar>
        <p id="navbarContent">Navbar Content</p>
        </div>
        <div id="gridContainer">
            <div class="grid grid-cols-8 grid-rows-5 gap-7 h-screen h-width">
                <div class="row-start-2 row-span-1 col-start-2 col-span-1">
                    <div class="flex flex-col relative mt-40 min-w-sm items-end justify-center">
                        <div class="group relative cursor-pointer">

                            <div class="flex items-center justify-center rounded-2xl group-hover:rounded-b-none bg-slate-700 px-4 min-w-36">
                                <a class="menu-hover my-2 py-2.5 text-slate-400 lg:mx-4" onClick="">
                                    {{ truechosenSubject }}
                                </a>
                                <span>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                        stroke="currentColor" class="h-6 w-6">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
                                    </svg>
                                </span>
                            </div>

                            <div
                                class="invisible absolute z-50 flex w-full flex-col bg-slate-800 py-1 px-4 text-gray-800 shadow-xl group-hover:visible rounded-b-2xl">

                                <a @click="updateSubject" id="physics" class="my-2 block border-b border-slate-800 py-1 font-semibold text-gray-500 hover:text-slate-400 md:mx-2">
                                    Physics
                                </a>

                                <a @click="updateSubject" id="economics" class="my-2 block border-b border-slate-800 py-1 font-semibold text-gray-500 hover:text-slate-400 md:mx-2">
                                    Economics
                                </a>

                                <a @click="updateSubject" id="p1" class="my-2 block border-b border-slate-800 py-1 font-semibold text-gray-500 hover:text-slate-400 md:mx-2">
                                    Pure Maths 1
                                </a>

                                <a @click="updateSubject" id="m1" class="my-2 block border-b border-slate-800 py-1 font-semibold text-gray-500 hover:text-slate-400 md:mx-2">
                                    Mechanics 1
                                </a>

                                <a @click="updateSubject" id="s1" class="my-2 block border-b border-slate-800 py-1 font-semibold text-gray-500 hover:text-slate-400 md:mx-2">
                                    Statistics 1
                                </a>

                                <a @click="updateSubject" id="biology" class="my-2 block border-b border-slate-800 py-1 font-semibold text-gray-500 hover:text-slate-400 md:mx-2">
                                    Biology
                                </a>

                                <a @click="updateSubject" id="chemistry" class="my-2 block border-b border-slate-800 py-1 font-semibold text-gray-500 hover:text-slate-400 md:mx-2">
                                    Chemistry
                                </a>
                                <a @click="updateSubject" id="" class="my-2 block border-b border-slate-800 py-1 font-semibold text-gray-500 hover:text-slate-400 md:mx-2">
                                    ALL
                                </a>

                            </div>
                        </div>
                    </div>
                </div>
                <div class="row-start-2 row-span-1 col-start-7 col-span-1">
                    <button @click="handleCheckboxChange" ref="MStoggler" :class="{ 'flex mt-40 items-center justify-center rounded-2xl group-hover:rounded-b-none bg-slate-700 px-4 min-w-36 text-slate-400 py-5 duration-150': true, 'bg-slate-800 scale-95': includeMS }">
                        {{ ptypeState }}
                    </button>
                </div>
                <div class="row-start-2 col-start-3 col-end-7">
                    <SearchBar class="col-span-full"></SearchBar>
                </div>


            </div>
        </div>
        <div  class="fixed bottom-0 right-0  bg-black text-white z-50">
        <button @click="scrollToTop" class="px-4 py-2 hover:bg-white hover:text-black z-50 border-2 border-slate-600">
            TOP
        </button>
        <button @click="scrollToClosestQ" class="px-4 py-2 hover:bg-white hover:text-black z-50 border-2 border-l-0 border-slate-600">
            NEXT QUESTION
        </button>
        <button @click="scrollToClosestMatch" class="px-4 py-2 hover:bg-white hover:text-black z-50 border-2 border-l-0 border-slate-600">
            NEXT MATCH
        </button>
        </div>
        
        <div v-if="loading" class='flex justify-center items-center fixed top-0 w-full h-full z-50 bg-slate-800'>
            <span class='sr-only'>Loading...</span>
            <div class='h-8 w-8 bg-slate-500 rounded-full animate-bounce [animation-delay:-0.3s]'></div>
            <div class='h-8 w-8 bg-slate-500 rounded-full animate-bounce [animation-delay:-0.15s]'></div>
            <div class='h-8 w-8 bg-slate-500 rounded-full animate-bounce'></div>
        </div>
        <div v-show="showResultsContainer" id="gridContainer2" class="relative grid-cols-4 grid flex-col px-20 p-4 min-h-0" ref="gridContainer2">
            <div
                v-for="(article, index) in articles"
                :key="article.id"
                class="scrollTarget min-w-96 col-start-1 col-end-5  text-ellipsis overflow-hidden pt-20 whitespace-pre-wrap">
                    <div>
                        <h1 class="text-2xl py-2 pb-5 font-extrabold tracking-wider text-emerald-500">{{ 'Q.' + article.qno + ' --- ' + article.papercode }}</h1>
                        <h3 class="text-gray-300" v-html="highlightedText(article.content, article.highlights[0].texts[1].value)"> </h3>
                    </div>  
                    <div>
                        <hr class="my-12 h-px border-t-0 bg-white opacity-25 dark:opacity-100" />
                    </div>    
            </div>
        </div>


    </div>

</template>



<script>


import eventBus from './eventBus.js';

export default {
    data() {
            return {
                articles: [],
                currentRowIndex: 0,
                loading: false,
                showResultsContainer: false,
                truechosenSubject: 'ALL',
                chosenSubjectUrlName: 'ALL',
                ptypeState: "excluding MS",
                includeMS: false
            }
    },
    created() {
        eventBus.on('custom-event', this.handleSearch);
    },
    methods: {
        handleSearch(searchText) {


            // Fetch data using the search text
            this.loading = true;

            const params = {
                order: -1,
                field: 'content',
                query: searchText,
                subject: this.chosenSubjectUrlName,
                type: 'QP'
            }

            if (this.chosenSubjectUrlName == "" || this.chosenSubjectUrlName == null || this.chosenSubjectUrlName == "ALL") {
                delete params.subject
            }
            if (this.ptypeState == "including MS") {
                delete params.type
                console.log("including markschemes too")
            }


            console.log(searchText)
            const searchParams = new URLSearchParams(params);


            this.articles=[];
            console.log(searchParams.toString())
            fetch(`http://pastpaperapi.onrender.com/search?${searchParams.toString()}`, {
                method: "GET",
                headers: {
                "Content-Type": "application/json",
                },
            })
            .then(resp => resp.json())
            .then(data => {
                console.log(data)
                this.articles.push(...data)
                // Update the state or perform other actions with the fetched data
            })
            .catch(error => {
                console.error(error);
            })
            .finally(() => {
                this.loading = false;
                this.showResultsContainer = true;
                setTimeout(() => {
                    this.$refs.gridContainer2.scrollIntoView({ behavior: 'smooth', block: 'start'})
                }, 3000)

            });
        },
        updateSubject(event) {
            // Update the variable with the content of the 'a' tag
            this.truechosenSubject = event.target.textContent;
            this.chosenSubjectUrlName = event.target.id;
        },
        handleCheckboxChange () {
            this.includeMS = !this.includeMS
            if (this.ptypeState == "excluding MS") {
                this.ptypeState = "including MS"
            }
            else {
                this.ptypeState = "excluding MS"
            }
        },
        scrollToClosestQ() {
            // Get all elements with the class 'scrollTarget'
            const targets = this.$refs.gridContainer2.querySelectorAll('.scrollTarget');

            // Find the closest target below the current viewport
            let closestTarget = null;
            let closestDistance = Infinity;

            targets.forEach(target => {
            const rect = target.getBoundingClientRect();
            const distance = rect.top - window.innerHeight;

            // Check if the target is below the current viewport
            if (distance > 0 && distance < closestDistance) {
                closestDistance = distance;
                closestTarget = target;
            }
            });

            // Scroll to the closest target
            if (closestTarget) {
            closestTarget.scrollIntoView({ behavior: 'smooth' });
            }
        },
        scrollToClosestMatch() {
            const textMatches = document.querySelectorAll('.textMatch');

            let closestTarget = null;
            let closestDistance = Infinity;

            textMatches.forEach(target => {
                const rect = target.getBoundingClientRect();
                const distance = Math.abs(rect.top)

                if (rect.top >= 111 && distance < closestDistance) {
                closestDistance = distance;
                closestTarget = target;
                }
            });

            if (closestTarget) {
                window.scrollTo({ top: closestTarget.getBoundingClientRect().top + window.scrollY - 110, behavior: "smooth"});
            }
        },
        scrollToTop() {
            this.$refs.gridContainer2.scrollIntoView({ behavior: 'smooth', block: 'start'})

        },
        highlightedText(string1, string2) {
            // Escape special characters in string2 to avoid issues with RegExp
            const escapedString2 = string2.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

            // Create a RegExp to match all occurrences of string2 in string1
            const regex = new RegExp(escapedString2, "gi");

            // Replace occurrences with the highlighted version
            const highlightedContent = string1.replace(
                regex,
                (match) => `<span class="textMatch text-orange-500 decoration-sky-500 underline text-2xl font-extrabold">${match}</span>`
            );

            return highlightedContent;
        }
    },

};
</script>