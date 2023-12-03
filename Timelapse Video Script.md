### Intro
1. Beautiful landscapes and road footage.
  Voiceover: I'm keen on exploring beautiful places and this time, I went for a small trip to mountains. Everything was perfect, except one little thing I will try to fix in this video
### Scene 1
1. Person 2 is putting SD card into a slot, close-up.
2. A person is sitting at the table, another person joins and takes a seat near him.
  Person 1: Hey, what's up?
  Person 2: I filmed a beautiful timelapse, but I slightly changed a camera shutter speed a few times while shooting, and now it's ruined.
  Person 1: Let me take a look.
3. Person 2 rotates his laptop a bit and shows the video.
  Person 1: Ah, I see. I think I can help you.
  Person 2: Really?
  Person 1: By the way, nice laptop
4. Person 1 opens his laptop's lid

### Scene 2
(Requires proofreading/grammar fixes)
First up, let's define the issue we are going to solve. We have a few thousands of photos taken with some intervals and we want to create a stunning timelapse video from these photos. To begin, let's resize all these images because it's a pretty cpu-consuming task and let's do this once and forget about it for the rest of the video.

Moving on, let's create the timelapse without any adjustments and check the result

And here are these exposure, shutter speed changes kick in. It's just these sudden blackouts you can observe

Here I want to visualize the brightness distribution across all images to find these pick and take a look at the specific photos that have visible brightness differences

These dips in the plot. Are actually these images. And let's take a look at the first one. As you can tell, here is the visible brightness change

I decided to fix this issue using histogram matching algorithm. Let's start from calculating histograms of these two images that have different brightness.

The brighter image has more values on the right side of the plot and vice-versa for the second one. Great. Now our task is just to adjust each pixel of the first image the way to math these histograms.

So, here is a brief explanation of the algorithm itself and it's implementation below. And since I want to keep this video short be more like vlog, I'm not going to dive deep in the math behind this algorithm but if fell free to left the comment if it will be interesting for someone and I'll make a video. If this video will not be the last one on this channel. Let's go further (such a difficult word to pronounce).

Here are the histograms after the first image is being adjusted (CORRECT THIS SENTENCE). Excellent.

Now, we are ready to apply this solution to the whole footage we have. I'm going to use the last image with visible brightness difference as a reference image and apply it to all preceding images. But feel free experiment and there might be lots different approaches giving us different interesting results.

And finally, let's see how it turned out.
### Outro
Great, the footage is saved. I'll left a github link with this notebook below this video. And see ya!
