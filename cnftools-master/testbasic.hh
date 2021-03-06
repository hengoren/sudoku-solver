/*
  Copyright (C) 2013 by Massimo Lauria <lauria.massimo@gmail.com>
  
  Created   : "2013-08-01, giovedì 17:29 (CEST) Massimo Lauria"
  Time-stamp: "2013-08-01, 19:12 (CEST) Massimo Lauria"
  
  Description::
  
  Test basic library facilities and CNF object implementation (using cppunit)
  
*/

#ifndef _TESTBASIC_HH_
#define _TESTBASIC_HH_

#include <cppunit/TestFixture.h>
#include <cppunit/extensions/HelperMacros.h>


class TestBasic : public CppUnit::TestFixture  {
  
  CPPUNIT_TEST_SUITE( TestBasic );
  CPPUNIT_TEST( test_list_constructor );
  CPPUNIT_TEST( test_clause_addition );
  CPPUNIT_TEST_SUITE_END();
 
public:
  virtual void setUp();
  virtual void tearDown();
  virtual void test_list_constructor();
  virtual void test_clause_addition();
};

CPPUNIT_TEST_SUITE_NAMED_REGISTRATION( TestBasic,
                                       "Testing CNF object implementation" );


#endif /* _TESTBASIC_HH_ */










