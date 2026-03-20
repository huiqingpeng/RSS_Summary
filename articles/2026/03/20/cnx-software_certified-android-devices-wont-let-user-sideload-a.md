---
title: "Certified Android devices won’t let user sideload APK app files anymore, or at least it won’t be straightforward"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/20/certified-android-devices-wont-let-user-sideload-apk-app-files-anymore-or-at-least-it-wont-be-straightforward/"
published: "2026-03-20"
fetched: "2026-03-20T21:03:08.221496"
---

Google won’t allow people to (easily) sideload apps through APK files on certified Android devices starting in September 2026. It will still be possible, but either require “developer verification” and an “advanced flow” for power users.
I was recently made aware of the issue after a BravePipe (previously BraveNewPipe) update, where I was greeted by a pop-up entitled “Keep Android Open” and linking to a website for more details.
The “Keep Android Open” website explains that the following will be required to install and update an app (APK) on a certified device:
- Paying a fee to Google
- Agreeing to Google’s Terms and Conditions
- Providing government identification
- Uploading evidence of the developer’s private signing key
- Listing all current and future application identifiers
This afternoon, I saw an X post about the topic providing more details, and appearing to follow a new post on the Android Developers Blog entitled “Android developer verification: Balancing openness and choice with safety” and featuring a banner reading “sideloading is here to stay”.
Google lists three ways to sideload apps:
- Sideloading directly from verified developers – It just works as usual, but developers will need to be verified, which can cause issues for some apps
- Sideloading from developers with limited distribution accounts – Sideload from developers the user knows, and from channels they choose. This was not super clear to me, but Google explains further:
we’re building free, limited distribution accounts for students and hobbyists. This allows you to share apps with a small group (up to 20 devices) without needing to provide a government-issued ID or pay a registration fee.
- Sideloading from unverified developers with advanced flow – That may be a random APK downloaded from GitHub.
The “Keep Android Open” website clearly mentioned the first option. The third way used to be the most common way: simply download an APK, accept the risks, and install it. This creates a security issue, so Google designed an “advanced flow” for these:
- Enable developer mode in system settings
- Confirm you aren’t being coached – In other words, they want to make sure the user is not being pushed by scammers to install the app.
- Restart your phone and reauthenticate – Used to cut off any remote access or active phone calls a scammer might be using
- One-time, one-day wait. You read that correctly, you’d need to wait for 24 hours after restarting your phone. That’s the “Security delay” step.
- After the delay, confirm that this is really you with biometric authentication (fingerprint or face unlock) or device PIN.
- Install apps – You will then be able to install apps from unverified developers, with the option of enabling this feature for 7 days or indefinitely.
That’s inconvenient, but at least people won’t need to pay to sideload apps, and developers who prefer to remain anonymous will be able to do so. On the plus side, it may reduce the effectiveness of scammers.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
