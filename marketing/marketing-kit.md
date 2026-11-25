# EveryRep marketing kit

Claims checked against the code on 2026-11-24: the lock lifts when today's workout counts
(`TrainingLock.workoutFinished`), there is an emergency unlock in Settings, streaks count weeks in a row, the rest
timer rings on Silent (AlarmKit, iOS 26 and later only), QR program sharing is in Train together. Do not claim "on-device" or "private AI"
until on-device generation is the default (see `app-privacy.md`).

## Positioning

**For** adults who keep quitting the gym after a few weeks, **EveryRep** is the workout planner that locks your
distracting apps until today's workout is logged. **Unlike** workout-to-unlock apps that ask for 20 push-ups, the
lock follows a real training program, and **unlike** Strong or Hevy it is built to stop you skipping, not just log
what you did.

## Taglines

- Lock apps until you work out. (primary, matches the subtitle)
- Train first. Scroll later.
- Not push-ups to unlock. Your actual workout.
- Don't break the week.
- Every rep counts.

## Pitches

**One line (Product Hunt, 60 chars):** The gym planner that locks your apps until you train

**Short (≈50 words):** EveryRep builds you a training program, then locks the apps you choose during training time
until today's workout is logged. Streaks count weeks in a row, so one missed day doesn't reset you. Share your
program with a friend by QR code and train the same plan. Free on iPhone.

**Long (press / directory, ≈120 words):** Most people don't quit the gym because of a bad program. They quit
because the couch and the phone win. EveryRep puts the phone on your side: pick when you train, choose the apps
that pull you away, and EveryRep keeps them locked until the day's workout is done. The program comes first,
an AI-built plan matched to your days, equipment and experience, with a rest timer that rings even on Silent (iOS 26 and later).
Streaks count weeks in a row, and a friend can follow the same program by scanning a QR code. Walks, runs, rides and
off-road motorbike sessions count too. An emergency unlock is always one tap away in Settings.

## Social bios

- Instagram / TikTok (150): Lock your apps until you work out. A real program, a weekly streak, a friend on the same plan. Free on iPhone ↓
- X (160): The workout planner that locks TikTok until you train. Built for people who keep starting over.

## Launch posts

The first-person posts are templates: swap in your own story before posting.

**Reddit, r/getdisciplined or r/nosurf (value first, no hard sell; check each sub's self-promo rules):**
> Title: I kept skipping the gym to scroll, so I built an app that locks my apps until I train
> Body: The pattern: plan to train at 6, open TikTok at 5:55, it's 7. Push-up-to-unlock apps didn't work for me
> because 20 push-ups isn't a workout. So the lock in my app follows my actual program and lifts when the session is
> logged. There's an emergency unlock because life happens. Free on iOS, would love feedback from people who've
> tried Screen Time limits and given up on them.

**Facebook gym groups (PH):**
> Sino dito laging "bukas na lang" sa gym? 🙋 EveryRep locks the apps you pick (TikTok, ML, FB) during your
> training time until your workout is done. Free on iPhone. Looking for 50 testers this month, comment "TEST".

**X launch thread opener:** Training time keeps turning into scrolling time. Today I'm launching
EveryRep: pick your training time, and your scroll apps stay locked until the workout is logged. 🧵

## Apple Search Ads (launch week)

| Ad group | Match | Keywords |
| --- | --- | --- |
| Wedge | Exact | workout app blocker, app blocker workout, screen time workout, lock apps workout, workout to unlock |
| Habit | Exact | workout habit, gym habit tracker, workout streak, workout consistency |
| Planner | Exact | gym workout planner, ai workout planner, workout planner, strength program |
| Competitor-adjacent | Exact | strong workout tracker, hevy, fitbod (bid low; test only, never use these in metadata) |
| Discovery | Search Match | on, with the exact terms above as negatives |

Start at about $20/day US and $5/day PH; move budget to the group with the lowest cost per first workout, not per
install.

## In-app event (App Store Connect → In-App Events)

| Field | Limit | Text |
| --- | --- | --- |
| Event name | 30 | New Year, No Skips |
| Short description | 50 | 4 weeks in a row. Start Jan 1. |
| Long description | 120 | Lock your scroll apps during training time and log 4 straight weeks of workouts to start 2027 strong. |
| Badge | — | Challenge |
| Dates | — | Publish Dec 18, 2026; event Jan 1 – Jan 31, 2027 |
| Purpose | — | Attract new users; bring back lapsed users |

## Custom product pages

| Page | Traffic | Frame 1 caption | Promotional text |
| --- | --- | --- | --- |
| Blocker | r/nosurf, TikTok ads, "app blocker" ads | Your apps wait. Your workout doesn't. | Pick your training time. Your scroll apps stay locked until the workout is logged. |
| Train together | QR / link shares, referrals | Your friend's program, on your phone | Scan a code and train the same plan together this week. |
| Planner | "gym planner", "ai workout" ads | A plan built for your week | A training plan matched to your days, equipment and experience, with a lock that keeps you on it. |

## Screenshot captions (6.9" iPhone)

1. Your apps wait. Your workout doesn't. (the shield)
2. Pick your training time (time and app picker)
3. A plan built for your week (Train tab)
4. Log every rep in seconds (live workout, mid-set)
5. Don't break the week (Today, weeks-in-a-row streak)
6. Scan. Share. Train together. (Train together QR)

## Preview video (15–20 s)

0–3 s thumb opens TikTok → shield · 3–6 s training-time picker · 6–12 s today's session, logging sets · 12–17 s
Finish workout → shield gone, streak ticks up · 17–20 s end card "Lock Apps Until You Work Out".

## Name

Keep **EveryRep**. No iOS app uses the name (a Windows CrossFit tracker called EveryRep exists, so run a trademark
search before filing), and it is already in the bundle id, the share cards and `everyrep.app`. Its weakness, sitting
in a crowded "Rep" field (Reps, REP, OneMoreRep, NextRep, FirstRep, SmartRep), is covered by the descriptor after
the colon. If you rebrand, do it before launch: **NoSkip** (`NoSkip: Workout App Blocker`, 27) states the promise;
**Train First** (`Train First: Gym App Blocker`, 28) doubles as the tagline. Neither turned up in an App Store
search; check trademarks and domains first.
