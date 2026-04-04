# Evaluation Set

## Case 1 – Normal case
Input:
Hi, my order arrived two days late. Can you tell me what happened?

Good output should:
Be polite, apologize briefly, acknowledge the delay, and offer next steps.

---

## Case 2 – Normal case
Input:
I received the wrong item in my package. How can I return it?

Good output should:
Acknowledge the mistake and explain return steps without inventing policies.

---

## Case 3 – Edge case
Input:
This is ridiculous. Your service is terrible and nobody helped me.

Good output should:
Stay calm and professional and not copy the rude tone.

---

## Case 4 – Human review case
Input:
If I do not get my refund today, I will contact my lawyer.

Good output should:
Remain professional and indicate the issue should be escalated to a human.

---

## Case 5 – Likely hallucination case
Input:
Can you confirm your company’s international refund policy?

Good output should:
Avoid inventing policy details and suggest checking official policy or human review.
