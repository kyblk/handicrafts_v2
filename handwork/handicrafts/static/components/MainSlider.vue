<template>
    <div id="main">
        <b-carousel id="carousel1"
                    style="text-shadow: 1px 1px 2px #333;"
                    controls
                    indicators
                    background="#ababab"
                    :interval="4000"
                    img-width="1024"
                    img-height="480"
                    v-model="slide"
                    @sliding-start="onSlideStart"
                    @sliding-end="onSlideEnd"
        >

            <!-- Text slides with image -->
            <b-carousel-slide caption="Katarina Fairy открылась!"
                              text="Успейте заказать крутые подарки"
                              img-src="https://picsum.photos/1024/480/?image=52"
            ></b-carousel-slide>

            <!-- Slides with custom text -->
            <b-carousel-slide
                    caption="Второй слайд"
                    img-src="https://picsum.photos/1024/480/?image=54">
            </b-carousel-slide>


        </b-carousel>

    </div>
</template>

<script>
    export default {
        data() {
            return {
                slide: 0,
                sliding: null
            }
        },
        methods: {
            onSlideStart(slide) {
                this.sliding = true
            },
            onSlideEnd(slide) {
                this.sliding = false
            }
        }
    }
</script>
