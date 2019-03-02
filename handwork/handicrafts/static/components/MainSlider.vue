<template>
    <div>

        <b-carousel id="carousel1"
                    style="text-shadow: 1px 1px 2px #333;"
                    controls
                    indicators
                    background="rgba(95, 1  58, 160, 0)"
                    :interval="4000"
                    img-width="1024"
                    img-height="480"
                    v-model="slide"
                    @sliding-start="onSlideStart"
                    @sliding-end="onSlideEnd"
        >
            <!-- Text slides with image -->
            <b-carousel-slide
                    v-for="slider in sliders"
                    :key="slider.id"
                    v-bind:caption="slider.text"
                    v-bind:img-src="slider.image"

            />
        </b-carousel>

    </div>
</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {
                slide: 0,
                sliding: null,
                sliders: [],
            }
        },
        methods: {
            onSlideStart(slide) {
                this.sliding = true
            },
            onSlideEnd(slide) {
                this.sliding = false
            },
            getSliders() {
                axios.get(this.$hostname_api + "/sliders/").then(res => this.sliders = res.data)
                    .catch(error => console.log(error))
            }
        },
        beforeMount() {
            this.getSliders()
        },
    }
</script>
<style>
    .carousel-caption {
        bottom: 220px;
    }

    .carousel-inner {
        border-radius: 5px;
    }
</style>