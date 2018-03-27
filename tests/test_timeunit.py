#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import timeunit
from should import it


class Test_TimeUnit(object):

    def test_simple_conversions(self):
        converted = timeunit.microseconds.to_nanos(1)
        it(converted).should.be.equal(1000)

        converted = timeunit.nanoseconds.to_micros(1000)
        it(converted).should.be.equal(1)

        converted = timeunit.seconds.to_millis(5)
        it(converted).should.be.equal(5000)

        converted = timeunit.milliseconds.to_seconds(5000)
        it(converted).should.be.equal(5)

        converted = timeunit.hours.to_minutes(1)
        it(converted).should.be.equal(60)

        converted = timeunit.minutes.to_hours(60)
        it(converted).should.be.equal(1)

        converted = timeunit.days.to_hours(1)
        it(converted).should.be.equal(24)

        converted = timeunit.hours.to_days(24)
        it(converted).should.be.equal(1)


    def test_convert_corectly(self):
        converted = timeunit.milliseconds.convert(5, timeunit.seconds)
        it(converted).should.be.equal(5000)

        converted = timeunit.seconds.convert(5000, timeunit.milliseconds)
        it(converted).should.be.equal(5)

    def test_sleep_1_seconds(self):
        start = time.time()
        timeunit.seconds.sleep(1)
        slept = time.time() - start
        it(slept).should.be.within(0.8, 1.2)

    def test_sleep_minus_sceonds(self):
        start = time.time()
        timeunit.seconds.sleep(-1)
        slept = time.time() - start
        it(slept).should.be.within(0, 0.2)

