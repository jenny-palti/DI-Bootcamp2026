# Daily Challenge: Real-world Data Analysis Scenarios
**Week 3, Day 1 – Data analysis, understanding and preprocessing**

## The case: Crisis Text Line uses data analysis to reach people at highest risk first

Crisis Text Line is a free, 24/7 text-message service in the US where people in emotional crisis can text and be answered by a trained volunteer counselor. Like any crisis service, it faces a basic problem: there are more people texting than counselors available, so some people have to wait. Traditionally, conversations were answered roughly in the order they arrived.

## What data was analyzed

Crisis Text Line has a very large archive of anonymized text conversations — tens of millions of messages. After each conversation, the counselor fills in a short survey, including whether the conversation involved suicide risk. This gave the organization something very valuable for data analysis: **real messages linked to a known outcome**.

## The methods used

- **Exploratory analysis:** they looked at which words and expressions appeared most often in the opening messages of conversations that later turned out to be high-risk.
- **Machine learning:** they trained a model (an ensemble of neural networks) on those labeled conversations, so it could predict risk from the first messages of a *new* conversation.
- **Continuous feedback:** counselors' post-conversation labels keep being fed back to retrain and improve the model.

## What the analysis uncovered

The most surprising finding was that the word **"suicide" itself was not the strongest signal**. Thousands of other words and word combinations — including certain medication names and even some emojis — predicted a life-threatening situation more strongly than the word "suicide" did. A human reading a queue of messages would naturally prioritize the person who wrote "suicide"; the data showed this intuition misses many of the people in greatest danger.

## The impact

Crisis Text Line used the model to **re-order the waiting queue**, so that texters predicted to be at high risk are answered first. Reported results:

- The model identifies around **86%** of texters at severe, imminent risk in their first conversation.
- Response time for high-risk texters dropped from just under **2 minutes to about 39 seconds**.
- The organization reported that most high-risk texters are now reached in **under 5 minutes**, even during sudden spikes in volume.

## What would have been different without data analysis?

Without the analysis, the queue would stay first-come, first-served, and counselors would rely on their own intuition about which words sound dangerous. The data showed that intuition is incomplete: some of the highest-risk people never use the most "obvious" words. In a crisis setting, a few minutes of waiting can matter enormously, so changing **who gets answered first** is a decision with real human consequences.

## Why this case matters

This story shows several things about data analysis:
1. **Labeled outcome data is the key asset.** The counselor surveys turned a pile of messages into something a model could learn from.
2. **Data can correct expert intuition**, not just confirm it.
3. **Analysis is most powerful when it changes a concrete decision** — here, the order of a queue.
4. **Ethics matter.** Mental health data is extremely sensitive. Crisis Text Line later faced public criticism (in 2022) over sharing anonymized conversation data with a for-profit spin-off, and ended that arrangement. This is a reminder that privacy and consent are part of responsible data analysis, especially in healthcare.

## Sources
- Crisis Text Line, "Detecting Crisis: An AI Solution" (2018): https://www.crisistextline.org/product/detecting-crisis-an-ai-solution/
- Suicide Prevention Resource Center, "AI Figured out the Word People Text When Their Suicide Risk Is High": https://sprc.org/?p=15176
- Mashable (via The Living Library), on words and emojis linked to high risk: https://thelivinglib.org/?p=48668
