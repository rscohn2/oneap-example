// SPDX-FileCopyrightText: 2020 Intel Corporation
//
// SPDX-License-Identifier: MIT

#include <iostream>

#include "daal.h"

using namespace daal;
using namespace daal::services;
using namespace daal::data_management;

int main() {
  std::cout << "Basic statistics example" << std::endl << std::endl;

  const size_t nObservations = 4;
  const size_t nFeatures = 4;
  float data[nFeatures * nObservations] = {7.0f, 3.0f, 6.0f, 2.0f, 1.0f, 3.0f,
                                           0.0f, 2.0f, 9.0f, 2.0f, 6.0f, 2.0f,
                                           3.0f, 4.0f, 7.0f, 2.0f};
  const char *csvString = "7,3,6,2\n1,3,0,2\n9,2,6,2\n3,4,7,2";

  /* Initialize StringDataSource to read data from a string in the csv format */
  StringDataSource<CSVFeatureManager> dataSource(
      (daal::byte *)csvString, DataSource::doAllocateNumericTable,
      DataSource::doDictionaryFromContext);
  dataSource.loadDataBlock();
  NumericTablePtr table = dataSource.getNumericTable();

  /* Get basic statistics from the table. They were calculated inside DataSource
   * for each column. */
  NumericTablePtr min = table->basicStatistics.get(NumericTableIface::minimum);
  NumericTablePtr max = table->basicStatistics.get(NumericTableIface::maximum);
  NumericTablePtr sum = table->basicStatistics.get(NumericTableIface::sum);
  NumericTablePtr sumSquares =
      table->basicStatistics.get(NumericTableIface::sumSquares);

  /* Create NumericTable with the same data. But in this case basic statistics
   * are not calculated. */
  SharedPtr<HomogenNumericTable<>> dataTable =
      HomogenNumericTable<>::create(data, nFeatures, nObservations);

  /* Set basic statistics in the new NumericTable */
  dataTable->basicStatistics.set(NumericTableIface::minimum, min);
  dataTable->basicStatistics.set(NumericTableIface::maximum, max);
  dataTable->basicStatistics.set(NumericTableIface::sum, sum);
  dataTable->basicStatistics.set(NumericTableIface::sumSquares, sumSquares);

  return 0;
}
