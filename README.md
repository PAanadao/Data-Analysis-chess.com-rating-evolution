# Chess.com Rating Evolution Tracker

A simple Python script to generate a Chess.com rating progression graph based on the **total number of games played**, rather than calendar dates.

## Motivation

The platform's original graph uses a timeline (dates). When a player takes several months off, the visualization of their rating progression becomes distorted by long periods of inactivity.

By changing the X-axis to the **sequential number of games played**, it becomes easier to identify:

* Actual rating progression based on playing volume and experience.
* Learning plateaus and sudden rating drops (*tilt*).
* Continuous progress without the interference of inactivity periods.

## Requirements

Install the dependencies using pip:

```bash
pip install requests pandas matplotlib
```
