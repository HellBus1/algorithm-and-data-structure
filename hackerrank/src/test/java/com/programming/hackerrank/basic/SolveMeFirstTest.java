package com.programming.hackerrank.basic;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class SolveMeFirstTest {
  private final SolveMeFirst solveMeFirst = new SolveMeFirst();
  
  @Test
  void SolveMeFirst_shouldReturn5WhenInvokedWith2And3() {
    final int expectedValue = 5;

    int actualValue = solveMeFirst.solveMeFirst(2, 3);

    assertEquals(expectedValue, actualValue);
  }

  @Test
  void SolveMeFirst_shouldReturn10WhenInvokedWith2And8() {
    final int expectedValue = 10;

    int actualValue = solveMeFirst.solveMeFirst(2, 8);

    assertEquals(expectedValue, actualValue);
  }
}
